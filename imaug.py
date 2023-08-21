import imgaug.augmenters as iaa
import imageio
import imgaug as ia
import  random


def multi_aug_weather(image_path):
    image = imageio.imread(image_path)
    seq = [
        iaa.FastSnowyLandscape(lightness_threshold=140,
                               lightness_multiplier=2.5 ),
        iaa.Fog(),
        iaa.Clouds(),
        iaa.Snowflakes(flake_size=(0.1, 0.4), speed=(0.01, 0.05)),
        iaa.Rain(speed=(0.1, 0.3)),
        iaa.Cartoon(blur_ksize=3, segmentation_size=1,
                    saturation=2.0, edge_prevalence=1),
        iaa.AllChannelsCLAHE(clip_limit=(1, 10), per_channel=True),
        iaa.AdditiveGaussianNoise(scale=(5, 30))

    ]

    index = random.sample(seq,4)
    for i in index:
    print(index)
    aug = seq[6]
    images_aug = aug(image=image)
    return images_aug



# aug = iaa.FastSnowyLandscape(
#     lightness_threshold=140,
#     lightness_multiplier=2.5
# )

image_path = r'F:\APP\BaiduNetdiskDownload\detect_car\detect_car\dataset\phase2_train\phase2_trian_type\engineering_car\img_67.jpg'
image_aug = multi_aug_weather(image_path)
ia.imshow(image_aug)

# image = imageio.imread(image_path)
# image_aug = aug(image  = image)
# ia.imshow(image_aug)


# def rotat(image_path):
#     image = imageio.imread(image_path)
#     rotate = iaa.Affine(rotate=(15, 45))
#     image_rotate = rotate(image=image)
#     ia.imshow(image_rotate)
#     return image_rotate
#
# rotat(image_path)
#

