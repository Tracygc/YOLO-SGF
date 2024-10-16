# YOLO-SGF
YOLO-SGF: Lightweight network for object detection in complex infrared images based on improved YOLOv8
### 使用了ultralytics架构
 [YOLOv8 文档](https://docs.ultralytics.com) 上有关训练、验证、预测和部署的完整文档。

<details open>
<summary>安装</summary>

使用Pip在一个[**Python>=3.8**](https://www.python.org/)环境中安装`ultralytics`包，此环境还需包含[**PyTorch>=1.8**](https://pytorch.org/get-started/locally/)。这也会安装所有必要的[依赖项](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml)。

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Downloads](https://static.pepy.tech/badge/ultralytics)](https://pepy.tech/project/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
pip install ultralytics
```

如需使用包括[Conda](https://anaconda.org/conda-forge/ultralytics)，[Docker](https://hub.docker.com/r/ultralytics/ultralytics)和Git在内的其他安装方法，请参考[快速入门指南](https://docs.ultralytics.com/quickstart)。

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ultralytics?logo=condaforge)](https://anaconda.org/conda-forge/ultralytics) [![Docker Image Version](https://img.shields.io/docker/v/ultralytics/ultralytics?sort=semver&logo=docker)](https://hub.docker.com/r/ultralytics/ultralytics)

</details>

<details open>
<summary>Usage</summary>

### CLI

YOLOv8 可以在命令行界面（CLI）中直接使用，只需输入 `yolo` 命令：
`yolo` 可用于各种任务和模式，并接受其他参数，例如 `imgsz=640`。查看 YOLOv8 [CLI 文档](https://docs.ultralytics.com/usage/cli)以获取示例。

### Python

YOLOv8 也可以在 Python 环境中直接使用，并接受与上述 CLI 示例中相同的[参数](https://docs.ultralytics.com/usage/cfg/)：


## YOLO-SGF--Train

YOLO-SGF  训练使用train_detect.py进行python运行

YOLO-SGF模型架构见cfg/models/yoloSGF.yaml

loss的修改见utils/loss.py的BboxLoss里面的 bbox_iou函数修改
