====================
django-dogstorage
====================
dogstorage is a so called *development storage engine*.

Many people have the problem with gigantomanic production databases with 
gigabytes of pictures/files. It is a pain to keep the image files synchronised 
between development and production environments. 

Therefore I have written this storage engine. In case a file is not found, 
an image from placedog.com_ will be used/displayed
instead.

If you are sick of dogs, you might want to check out _django-kittenstorage_.

Setup
=====
It's on pypi.

    ``pip install django-dogstorage``

Feel free to clone from github too. Forking is welcome as well :-)

In your django settings file:

    ``DEFAULT_FILE_STORAGE = 'dogstorage.storages.GreyDog'``

Storage Engines
===============
dogstorage offers two engines:

1. ``dogstorage.storages.GreyDog``
2. ``dogstorage.storages.ColorDog``

Choose depending on the saturation you want. I prefer ``GreyDog`` since it 
does have a pretty classy look.

Settings
========
There is only one setting:

DOG_SIZE  
    Default: ``(1024, 1024)``

    A tuple of format `(width, height)`, specifiying the size of the image 
    requested from placedog__.


.. _placedog.com: http://placedog.com/
__ placedog.com_

