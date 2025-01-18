# ComfyUI-UVR5
the comfyui custom node for [UVR5](https://github.com/Anjok07/ultimatevocalremovergui) to separate vocals and background music
<div>
  <figure>
  <img alt='webpage' src="web.png?raw=true" width="600px"/>
  <figure>
</div>
    
## How to use
make sure `ffmpeg` is worked in your commandline
for Linux
```
apt update
apt install ffmpeg
```
for Windows,you can install `ffmpeg` by [WingetUI](https://github.com/marticliment/WingetUI) automatically

then!
```
git clone https://github.com/AIFSH/ComfyUI-UVR5.git
cd ComfyUI-UVR5
pip install -r requirements.txt
```
`weights` will be download from huggingface automatically!

## Thanks
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS.git)
- [ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui) also konwn as UVR5

