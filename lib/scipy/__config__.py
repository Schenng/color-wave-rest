# This file is generated by /private/var/folders/my/m6ynh3bn6tq06h7xr3js0z7r0000gn/T/pip-se4VTZ-build/-c
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

blas_mkl_info={}
lapack_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3']}
blas_opt_info={'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)], 'extra_compile_args': ['-msse3', '-I/System/Library/Frameworks/vecLib.framework/Headers']}
atlas_blas_threads_info={}
openblas_info={}
atlas_info={}
lapack_mkl_info={}
mkl_info={}
atlas_blas_info={}
atlas_threads_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    