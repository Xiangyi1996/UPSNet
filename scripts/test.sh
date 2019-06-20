#!/usr/bin/env bash
python upsnet/upsnet_end2end_test.py --cfg upsnet/experiments/upsnet_resnet50_cityscapes_4gpu.yaml \
--weight_path ./model/upsnet_resnet_50_cityscapes_12000.pth