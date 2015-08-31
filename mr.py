# -*- coding: utf-8 -*- 
#slb@slb.moe
import os
import codecs
import subprocess
from time import sleep


def OpenAndReadUtf8(filepath):
    """return unicode"""
    try:
        openfile = codecs.open(filepath,"r",encoding='utf-8')
        infile = openfile.read()
        openfile.close()
        return infile
    except:
        e = "\nRead file " + filepath + " error!!!\n"
        print e
        os.system("pause")

def WriteMbcs(filepath,writethings,encoding='mbcs'):
    try:
        openfile = codecs.open(filepath,"w",encoding=encoding)
        openfile.write(writethings)
        openfile.close()
        e = "\nWrite file " + filepath + " complete!!!"
        print e
        return 0
    except:
        e = "\nWrite file " + filepath + " error!!!"
        print e
        os.system("pause")
        return 1


def hconf(conf="mr.conf"):
    confs={}
    try:
        opconf = codecs.open(conf,"r",encoding='utf-8')
        confsr = opconf.readlines()
        opconf.close()
        for cf in confsr:
            cf = cf.split(u"#")[0]
            if cf.strip():
                cfAB = cf.strip().split(u"=",1)
                if cfAB[1]:
                    confs[cfAB[0].strip()] = cfAB[1].strip()
    except:
        e = conf + u" error \n\n"
        print e.encode("mbcs")
        os.system("pause")
    return confs



def filelist(sourepath,ext=None):
    wpg = os.walk(sourepath)
    fp = []
    try:
        while True:
            tmp = wpg.next()
            for i in tmp[-1]:
                if not ext:
                    fp.append(os.path.join(tmp[0],i))
                if ext:
                    iext = i.split(".")[-1].lower()
                    ext = ext.lower()
                    if ext == iext:
                        fp.append(os.path.join(tmp[0],i))
    except StopIteration:
        pass
    except :
        print "filelist error"
    return fp

###############################################
def make_avs(rawfile):
    avsS = r".\script_seeds\seed_avs.avs"
    avsr = OpenAndReadUtf8(avsS)

    fnne = os.path.splitext(rawfile)[0]
    assfile = fnne + u".ass"
    
    Osfp = u"<SOURCE_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>"
    Oafp = u"<SUBTITLE_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>"
    avsr = avsr.replace(Osfp,rawfile)
    avsr = avsr.replace(Oafp,assfile)
    

    avsfile = fnne.encode("mbcs") + ".avs"
    c = WriteMbcs(avsfile,avsr)
    if c:
        print "make_avs error!"
        os.system("pause")
    else:
        print "make_avs finish"

def make_x264ripbat(rawfile):
    batS = r".\script_seeds\seed_x264rip.bat"
    batr = OpenAndReadUtf8(batS)

    fnne = os.path.splitext(rawfile)[0]
    h264file = fnne + u".h264"
    avsfile = fnne + u".avs"

    Oh264fp = u"<OUTPUT_H264_FILE_PATH_DONOT_EDIT_THIS>"
    Oavsfp = u"<INPUT_AVS_FILE_PATH_DONOT_EDIT_THIS>"

    batr = batr.replace(Oh264fp,h264file)
    batr = batr.replace(Oavsfp,avsfile)
    
    x264ripbatfile = fnne.encode("mbcs") + "_x264rip.bat"
    c = WriteMbcs(x264ripbatfile,batr)
    if c:
        print "make_x264ripbat error!"
        os.system("pause")
    else:
        print "make_x264ripbat finish"

def make_getaudiobat(rawfile):
    batS = r".\script_seeds\seed_getaudio.bat"    
    batr = OpenAndReadUtf8(batS)

    fnne = os.path.splitext(rawfile)[0]
    aacfile = fnne + u".aac"

    Omediafp = u"<INPUT_MEDIA_FILE_PATH_DONOT_EDIT_THIS>"
    Oaudiofp = u"<OUTPUT_AUDIO_FILE_PATH_DONOT_EDIT_THIS>"

    batr = batr.replace(Omediafp,rawfile)
    batr = batr.replace(Oaudiofp,aacfile)
    
    getaudiobatfile = fnne.encode("mbcs") + "_audio.bat"
    c = WriteMbcs(getaudiobatfile,batr)
    if c:
        print "make_getaudiobat error!"
        os.system("pause")
    else:
        print "make_getaudiobat finish"

def make_mergebat(rawfile):
    batS = r".\script_seeds\seed_merge.bat" 
    batr = OpenAndReadUtf8(batS)

    fnne = os.path.splitext(rawfile)[0]
    h264file = fnne + u".h264"
    aacfile = fnne + u".aac"
    mp4file = fnne + u"_muxed.mp4"

    Oihfp = u"<INPUT_H264_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>"
    Oiafp = u"<INPUT_AAC_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>"
    Oomfp = u"<OUTPUT_MERGED_FILE_PATH_DONOT_EDIT_OR_REMOVE_THIS>"

    batr = batr.replace(Oihfp,h264file)
    batr = batr.replace(Oiafp,aacfile)
    batr = batr.replace(Oomfp,mp4file)

    mergebatfile = fnne.encode("mbcs") + "_mux.bat"
    c = WriteMbcs(mergebatfile,batr)
    if c:
        print "make_mergebat error!"
        os.system("pause")
    else:
        print "make_mergebat finish"


def gocmd(batfile):
    batfile = '"%s"' % batfile
    try:
        rip = subprocess.Popen( batfile ,shell=True)
        rip.wait()
    except:
        print "\n\n\n\nerror " + "at " + batfile
        os.system("pause")


def movefile(sourefile):
    sourefile = sourefile.encode("mbcs")

    fnne = os.path.splitext(sourefile)[0]
    fnp = os.path.split(sourefile)[0]

    mp4file = fnne + "_muxed.mp4"
    newfile = os.path.split(mp4file)[1]
    newpath = fnp + "\\riped"
    try:
        os.makedirs(newpath)
        print "maked " + newpath
    except:
        pass
    newpath = newpath + "\\" + newfile
    import shutil
    shutil.move( mp4file , newpath )


def HandleFile(sourefile):
    make_avs(sourefile)
    make_x264ripbat(sourefile)
    make_getaudiobat(sourefile)
    make_mergebat(sourefile)

    fnne = os.path.splitext(sourefile)[0].encode("mbcs")

    batfile = fnne + "_audio.bat"
    gocmd(batfile)

    batfile = fnne + "_x264rip.bat"
    gocmd(batfile)
    sleep(3)
    try:
        os.system("taskkill /IM MP_Pipeline.dll.slave.exe /t /f")
        sleep(3)
    except:
        print "Can not kill MP_Pipeline.dll.slave.exe,Is it stoped?\n\n"
        pass
    batfile = fnne + "_mux.bat"
    gocmd(batfile)

    movefile(sourefile)
    print sourefile.encode("mbcs") + " is Complete!!!!!!!!\n=================================================\n"


if __name__ == "__main__":
    print "rip start!!!!!!!!!!!!!!!!!!!!!\n=================================================\n"
    wb = hconf()["wb"]
    ext = hconf()["ext"]
    fl = filelist(wb,ext)
    for f in fl:
        print "Handling... ... ..."
        print f.encode("mbcs")
        HandleFile(f)
    print "\n=================================================\nRip All Over!\n\n\n\n"
    os.system("pause")
    os.system("pause")











