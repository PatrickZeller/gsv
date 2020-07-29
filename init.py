import nuke
import gsv

## add callback
nuke.addFilenameFilter(gsv.expand_vars)