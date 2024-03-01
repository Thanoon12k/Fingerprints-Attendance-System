import ctypes as ct
import random
import PIL.Image as Image
import PIL.ImageOps
import os



class FTRHANDLE(ct.c_void_p):
    pass

class FTRSCAN_IMAGE_SIZE(ct.Structure):
    _fields_ = (('nWidth', ct.c_int),
                ('nHeight', ct.c_int),
                ('nImageSize', ct.c_int))
def SCAN_IMAGE(img_name="temp/finger_000.bmp"):
    print("start scanning......")
   
    PFTRSCAN_IMAGE_SIZE = ct.POINTER(FTRSCAN_IMAGE_SIZE)
    lib = ct.WinDLL("ftrScanAPI")  # due to __stdcall, only matters if 32-bit Python and DLL
    lib.ftrScanOpenDevice.argtypes = ()
    lib.ftrScanOpenDevice.restype = FTRHANDLE
    lib.ftrScanCloseDevice.argtypes = FTRHANDLE,
    lib.ftrScanCloseDevice.restype = None
    lib.ftrScanGetImageSize.argtypes = FTRHANDLE, PFTRSCAN_IMAGE_SIZE
    lib.ftrScanGetImageSize.restype = ct.c_int
    lib.ftrScanGetImage.argtypes = FTRHANDLE, ct.c_int, ct.c_void_p
    lib.ftrScanGetImage.restype = ct.c_int

    handle = lib.ftrScanOpenDevice()
    size = FTRSCAN_IMAGE_SIZE() # allocate output parameter storage
    if not lib.ftrScanGetImageSize(handle, ct.byref(size)):
        raise RuntimeError('get size failed')
        return (False)
    NDos = 4 # I don't know what this parameter means, from C# example
    buffer = ct.create_string_buffer(size.nImageSize) # storage for image
    if not lib.ftrScanGetImage(handle, NDos, buffer):
        raise RuntimeError('get image failed')
        return(False)
    img =Image.frombuffer("L", (320,480), buffer, 'raw', "L", 0, 1)
    # img = img.resize((320, 480))
    img.save(img_name)
    print("fingerprint scanned and saved in :",img_name)
    inverted_image = PIL.ImageOps.invert(img)
    inverted_image.save(img_name)
    lib.ftrScanCloseDevice(handle)
    return (True)
