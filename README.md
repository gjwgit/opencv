Open Computer Vision
====================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the functionalities of the Open Computer Vision toolkit.

Currently it only demonstrates the measuring of blurriness of images
through the blurry command.

Visit the github repository for more details:
<https://github.com/gjwgit/opencv>

Usage
-----

- To install mlhub (Ubuntu 18.04 LTS)

```console
$ pip3 install mlhub
```

- To install and configure the demo:

```console
$ ml install   gjwgit/opencv
$ ml configure opencv
```

Determine an Image's Blurriness
==============================

The returned measure might also be useful as a measure of how sharp
the image is?

![](http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg)
```console
$ ml blurry opencv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
Okay 1303
```
![](https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg)
```console
$ ml blurry opencv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
Okay 374
```
![](https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg)
```shell
$ ml blurry opencv https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg
Okay 170
```
![](https://www.nyip.edu/images/cms/photo-articles/stop-taking-blurry-pictures.jpg)
```sh
$ ml blurry opencv https://www.nyip.edu/images/cms/photo-articles/stop-taking-blurry-pictures.jpg
Blurry 68
```

![](http://getwallpapers.com/wallpaper/full/4/5/4/314199.jpg)
```sh
$ ml blurry opencv http://getwallpapers.com/wallpaper/full/4/5/4/314199.jpg
Blurry 43
```
