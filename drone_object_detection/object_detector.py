# Object Detection
# Imports
import os
import tensorflow as tf
import numpy as np

# Object detection imports
from drone_object_detection.utils import ops as utils_ops
from drone_object_detection.utils import label_map_util
from drone_object_detection.utils import visualization_utils as vis_util

# Model preparation
# What model to download.
OS_PATH = os.path.dirname(__file__)
MODEL_NAME = OS_PATH + '/export_dir/ssd_mobilenet_v2_coco_2018_03_29'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = OS_PATH + '/data/label_map.pbtxt'

# Using more UPU memory
GPU_config = tf.compat.v1.ConfigProto()
GPU_config.gpu_options.allow_growth = True

class Detector:
    def __init__(self):
        # Load a (frozen) Tensorflow model into memory
        self.detection_graph = tf.Graph()
        self.tensor_dict = {}
        self.sess = None
        with self.detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            
            self.sess = tf.Session(config=GPU_config)
            self.default_graph = tf.get_default_graph()
            ops = self.default_graph.get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            for key in [
              'num_detections', 'detection_boxes', 'detection_scores',
              'detection_classes', 'detection_masks'
              ]:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    self.tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)

        # Loading label map
        self.category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

    def load_image_into_numpy_array(self, image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

    def run_inference_for_single_image(self, image):
        if 'detection_masks' in self.tensor_dict:
            print("run_inference in detection_masks if block")
            # The following processing is only for single image
            detection_boxes = tf.squeeze(self.tensor_dict['detection_boxes'], [0])
            detection_masks = tf.squeeze(self.tensor_dict['detection_masks'], [0])

            # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
            real_num_detection = tf.cast(self.tensor_dict['num_detections'][0], tf.int32)
            detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
            detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
            detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                detection_masks, detection_boxes, image.shape[0], image.shape[1])
            detection_masks_reframed = tf.cast(
                tf.greater(detection_masks_reframed, 0.5), tf.uint8)

            # Follow the convention by adding back the batch dimension
            self.tensor_dict['detection_masks'] = tf.expand_dims(
                detection_masks_reframed, 0)

        image_tensor = self.default_graph.get_tensor_by_name('image_tensor:0')

        # Run inference
        output_dict = self.sess.run(self.tensor_dict,
                                    feed_dict={image_tensor: image})

        # all outputs are float32 numpy arrays, so convert types as appropriate
        output_dict['num_detections'] = int(output_dict['num_detections'][0])
        output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
        output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
        output_dict['detection_scores'] = output_dict['detection_scores'][0]
        if 'detection_masks' in output_dict:
            output_dict['detection_masks'] = output_dict['detection_masks'][0]
        return output_dict

    def run_object_detector(self, image, target_class_input):
        image_expanded = np.expand_dims(image, axis=0)
        output_dict = self.run_inference_for_single_image(image_expanded)
        target_finded, drone_controller = vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index,
            instance_masks=output_dict.get('detection_masks'),
            use_normalized_coordinates=True,
            line_thickness=2,
            min_score_thresh=0.50,
            target_class=target_class_input
        )
        output_dict['image'] = image
        output_dict['target_finded'] = target_finded
        output_dict['drone_controller'] = drone_controller
        # return image
        return output_dict
    
    def closeDetector(self):
        self.sess.close()