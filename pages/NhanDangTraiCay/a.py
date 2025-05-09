from ultralytics import YOLO

model = YOLO("D:\\NAM_HAI\\XLAS\\TraiCay\\Bản sao của best.pt")
path = model.export(format="onnx")