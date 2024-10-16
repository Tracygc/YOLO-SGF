from ultralytics.models.yolo.detect import DetectionTrainer

if __name__ == '__main__':
    args = dict(
        model='ultralytics/cfg/models/yoloSGF.yaml', # ，s
        # model='ultralytics/cfg/models/v8/yolov8.yaml',  #  原始v8
        data='ultralytics/cfg/datasets/my_yolo_my_5classes_enhance_all_721.yaml',
        imgsz=640,
        epochs=300,
        batch=8,
        workers=0,
        device=0,
        optimizer='SGD',  # 这里可以使用两个优化器SGD 和AdamW,其它的可能会导致模型无法收敛
    )
    trainer = DetectionTrainer(overrides=args)
    trainer.train()

