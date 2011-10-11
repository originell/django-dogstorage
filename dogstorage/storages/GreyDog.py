import tempfile
import urllib2

from django.core.cache import cache
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from dogstorage.settings import DOG_SIZE


class GreyDog(FileSystemStorage):
    """
    If a file is not found on disk, return a greyscale dog picture.
    """
    def _open(self, name, mode='rb'):
        if not self.exists(name):
            dogz = cache.get('dogz', False)
            if not dogz:
                # Grab a dog from placedog.
                # /g/ means grayscale
                response = urllib2.urlopen('http://placedog.com/g/%s/%s'
                                           % (DOG_SIZE[0], DOG_SIZE[1]))
                dog_img = response.read()
                cache.set('dogz', dog_img)
                dog = tempfile.TemporaryFile()
                dog.write(dog_img)
                # .write places the readhead at the end. Resetting it
                # to the start, otherwise an empty File() will be created.
                dog.seek(0)
                return File(dog)
            else:
                past_dog = tempfile.TemporaryFile()
                past_dog.write(dogz)
                past_dog.seek(0)
                return File(past_dog)
        return super(GreyDog, self)._open(name, mode)

