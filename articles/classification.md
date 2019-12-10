# Классификация методов

(Черновик)

1. По задаче
   *  \- Наземная (карты, аеросъемка)
   *  ✔ Прикладная (архитектура)

2. По количеству камер
* 1 камера (монофотограмметрия)
* 2+ камеры (стереофотограмметрия - SPG)

3. По типе камеры
* 2D камера (Two-dimensional photogrammetry)
* 3D камера RGBD (Three-dimensional photogrammetry, pointclouds)
* Laser scanner (LiDAR)


4. По способу ориентирования
   
    4.1. Источники с изображения
    * Point Tracking (Markers, Contrast points)
    * Digital Image Correlation (RANSAC, features)
    * Target-Less Approaches (Edge detection algorithm, Hough Transform - segmentation)

    4.2 Внешние источники
    * Sensors (Acc+Gyro)
    * GPS
