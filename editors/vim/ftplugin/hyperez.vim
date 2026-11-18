if exists("b:did_ftplugin")
  finish
endif
let b:did_ftplugin = 1
setlocal commentstring=//\ %s
setlocal comments=s1:/*,mb:*,ex:*/,:///,://
setlocal expandtab shiftwidth=4 softtabstop=4 tabstop=4
setlocal suffixesadd=.hez,.hz
setlocal makeprg=hyper\ check\ %
setlocal errorformat=%f:%l:%c:\ %m
let b:undo_ftplugin = "setlocal commentstring< comments< expandtab< shiftwidth< softtabstop< tabstop< suffixesadd< makeprg< errorformat<"
