<h1 align="center"> Image Processing Project </h1>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Introduction"> ➤ Introduction </a></li>
    <li><a href="#Objectives and scope"> ➤ Objectives and scope </a></li>
    <li><a href="#Methodology"> ➤ Methodology </a></li>
    <li><a href="#Down Sampling"> ➤ Down Sampling </a></li>
    <li><a href="#Up Sampling"> ➤ Up Sampling </a></li>
    <li><a href="#Negative of an Image"> ➤ Negative of an Image </a></li>
    <li><a href="#Thresholding"> ➤ Thresholding </a></li>
    <li><a href="#Blurring"> ➤ Blurring </a></li>
    <li><a href="#Low Pass Filtering (LPF)"> ➤ Low Pass Filtering (LPF) </a></li>
    <li><a href="#Gaussian Noise"> ➤ Gaussian Noise </a></li>
    <li><a href="#Laplacian Filter"> ➤ Laplacian Filter </a></li>
    <li><a href="#Conclusion"> ➤ Conclusion </a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- Introduction -->
<h2 id="Introduction"> :pencil: Introduction </h2>

<p align="justify"> 
  Edge detection is an essential part of image processing that involves finding the boundaries of objects 
within an image. This process can be used to extract useful information from an image, such as object 
recognition or feature detection. One of the most common techniques for edge detection is the 
Laplacian filter, which is a second-order derivative filter used to detect changes in the intensity of the 
image.
  
In this project, we will explore edge detection using the Laplacian filter and other image processing 
techniques such as low pass filtering (LPF), high pass filtering (HPF), and thresholding. LPF and HPF 
are commonly used to enhance images and remove noise, while thresholding is used to binarize an 
image into black and white pixels based on a certain threshold value.
  
The project will involve implementing these techniques using MATLAB and applying them to various 
test images to demonstrate their effectiveness in edge detection. The results will be analyzed and 
compared to determine the most effective approach for edge detection in different scenarios.
The objectives of this project are to gain a deeper understanding of image processing techniques, 
specifically edge detection using the Laplacian filter, LPF, HPF, and thresholding, and to demonstrate 
the practical applications of these techniques in real-world scenarios. 
  
  Through this project, we hope to 
enhance our skills in image processing and analysis, as well as gain insights into the challenges and 
limitations of edge detection techniques.

</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<!-- Objectives and Scope -->
<h2 id="Objectives and Scope"> :cloud: Objectives and Scope</h2>

<p align="justify"> 
  Utilizing image processing techniques such as low-pass filtering (LPF), blurring, and other such 
techniques to reduce noise and improve the overall quality of the images, as well as using edge 
detection to define boundaries for the images' borders.
  
A number of different methods, including thresholding and edge detection, are utilised in the 
process of segmenting and extracting information from images.
  
The distinction between the different subcategories can be seen through the employment of a 
variety of user-defined functions as well as built-in functions (LPF, Edge detection, etc).

</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<!-- Methodology -->
<h2 id="Methodology"> :cloud: Methodology </h2>

<p align="justify"> 
  The methodology for this project involved several steps, including image acquisition, image preprocessing, edge detection using the Laplacian filter, LPF, HPF, and thresholding, and analysis of the 
results.
The first step in the methodology was to acquire test images to be used in the project. These images 
were chosen based on their complexity and variability to test the effectiveness of the different edge 
detection techniques.
  
The second step was image pre-processing, which involved applying noise reduction techniques such 
as median filtering and histogram equalization to enhance the quality of the images. This was done to 
ensure that the edge detection techniques were applied to clear and high-quality images.
  
The third step was edge detection using the Laplacian filter, LPF, HPF, and thresholding techniques. 
The Laplacian filter was applied to detect edges by finding changes in the intensity of the image, 
while LPF and HPF were used to remove noise and enhance the edges. Thresholding was used to 
binarize the image into black and white pixels based on a certain threshold value.
  
Finally, the results were analyzed and compared to determine the most effective approach for edge 
detection in different scenarios. This involved visually comparing the different edge detection 
techniques and evaluating their accuracy in detecting edges.
  
Overall, the methodology for this project was a combination of image acquisition, pre-processing, 
edge detection using the Laplacian filter, LPF, HPF, and thresholding, and analysis of the results to 
determine the effectiveness of each technique in edge detection.


</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


<!-- Down Sampling -->
<h2 id="Down Sampling"> :cloud: Down Sampling </h2>

<p align="justify"> 
  Down Sampling:
• The process of resampling in a multi-rate digital signal processing system is referred to as 
down sampling, compression, and decimation in digital signal processing.
  
• Both down sampling and decimation can refer to the full process of bandwidth reduction 
(filtering) and sample-rate reduction, or they can be used interchangeably with the term 
compression.
  
• The technique produces an estimate of the sequence that would have been generated by 
sampling the signal at a lower rate when applied to a sequence of samples of a signal or a 
continuous function (or density, as in the case of a photograph).
  
• In down-sampling technique, the number of pixels in the given image is reduced depending 
on the sampling frequency. Due to this, resolution and size of the image decreases.
  
• Output:
  
 ![image](https://github.com/Haleshot/Projects/assets/57552973/3411e8eb-9375-4527-9724-441978892c61)



</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
