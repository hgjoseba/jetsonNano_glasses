import jetson.inference
import jetson.utils
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("display://0")
#net = jetson.inference.detectNet('ssd-mobilenet-v2',threshold = 0.3)
net = jetson.inference.detectNet(argv=["--model=Model/ssd-mobilenet.onnx","--labels=Model/labels.txt","--input-blob=input_0","--output-cvg=scores","--output-bbox=boxes"],threshold=0.6)

while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img)
    display.Render(img)
    display.SetStatus("Objetct Detection | FPS = " + str(net.GetNetworkFPS()))
    
