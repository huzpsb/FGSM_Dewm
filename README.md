# FGSM_Dewm
防止AI（StableDiffusion）自动去除插画图片上的水印。  

是 [DeWm](https://github.com/huzpsb/DeWm) 的反向工作。  
本repo的反向工作（~~你搁着套娃呢？~~）：[DeTox](https://github.com/huzpsb/DeTox/)  
出于某些考量，代码暂不开源，只是占个坑。（写完了）  

原始图片：  
![or](https://github.com/user-attachments/assets/cf5648c0-f6c1-472c-a5f6-020ef11c75f5)  
水印演示图片：  
![done](https://github.com/user-attachments/assets/2a9be155-7b38-41a8-9631-cba64be3b575)  
高阈值下：  
![mask](https://github.com/user-attachments/assets/52f440cd-f077-4021-b4b2-a4286322b130)  
低阈值下：  
![mask](https://github.com/user-attachments/assets/13ee7c1a-853c-41e9-a05a-820284c9c732)  
反正就是别想只选中水印！欸嘿（  

ChatGPT：  
<img width="868" alt="image" src="https://github.com/user-attachments/assets/5334963a-4d90-404d-acba-5a75c4d10ae0">  
描述的文本明显更短，并且无法仿图。（你可以在DeTox中找到完整描述！）  
SD：  
<img width="1275" alt="image" src="https://github.com/user-attachments/assets/f19a0487-0b89-4bd0-900a-b4fbe5edca61">  
描述的文本更少，识别水印Tag错误。（你可以在DeTox中找到完整描述！）  
