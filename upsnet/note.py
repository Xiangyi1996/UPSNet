'''''
UPSNet contains 8 loss functions in total:
semantic segmentation head (whole image and RoI based pixel-wise classiﬁcation losses),
panoptic segmentation head (whole image based pixel-wise classiﬁcation loss),
RPN (box classiﬁcation, box regression) and
instance segmentation head (box classiﬁcation, box regression and mask segmentation).

['__background__', 'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle', 'bicycle']
train_loader.dataset.dataset.category_to_id_map:
    {'person': 1, 'rider': 2, 'car': 3, 'truck': 4, 'bus': 5, 'train': 6, 'motorcycle': 7, 'bicycle': 8}
num_classes: 9

label:
['roidb', 'rpn_labels_fpn4', 'rpn_bbox_targets_fpn4', 'rpn_bbox_inside_weights_fpn4', 'rpn_bbox_outside_weights_fpn4',
 'rpn_labels_fpn8', 'rpn_bbox_targets_fpn8', 'rpn_bbox_inside_weights_fpn8', 'rpn_bbox_outside_weights_fpn8', 
 'rpn_labels_fpn16', 'rpn_bbox_targets_fpn16', 'rpn_bbox_inside_weights_fpn16', 'rpn_bbox_outside_weights_fpn16', 
 'rpn_labels_fpn32', 'rpn_bbox_targets_fpn32', 'rpn_bbox_inside_weights_fpn32', 'rpn_bbox_outside_weights_fpn32', 
 'rpn_labels_fpn64', 'rpn_bbox_targets_fpn64', 'rpn_bbox_inside_weights_fpn64', 'rpn_bbox_outside_weights_fpn64', 
 'seg_gt', 'seg_gt_4x', 'gt_classes', 'mask_gt']
 
 roidb:
['boxes', 'segms', 'seg_areas', 'gt_classes', 'gt_overlaps', 'is_crowd', 'box_to_gt_ind_map']

loss: 
rpn_cls_loss\, rpn_bbox_loss\, cls_loss\, bbox_loss\, mask_loss\
fcn_loss\\, fcn_roi_loss(false)\\, panoptic_loss\
'''''

