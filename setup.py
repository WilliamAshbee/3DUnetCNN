from setuptools import setup

setup(
    name='3DUnetCNN',
    version='1.0',
    packages=['unet3d', 'unet3d.train', 'unet3d.utils', 'unet3d.utils.nipy', 'unet3d.utils.pytorch', 'unet3d.utils.wquantiles', 'unet3d.utils.nilearn_custom_utils', 'unet3d.models', 'unet3d.models.keras', 'unet3d.models.keras.senet', 'unet3d.models.keras.resnet', 'unet3d.models.pytorch', 'unet3d.models.pytorch.fcn', 'unet3d.models.pytorch.graph', 'unet3d.models.pytorch.autoencoder', 'unet3d.models.pytorch.segmentation', 'unet3d.models.pytorch.classification', 'unet3d.scripts'],
    url='https://github.com/ellisdg/3DUnetCNN',
    license='',
    author='forked',
    author_email='',
    description='forked project with unet3d'
)
