# vim 配置

```bash
" 参考博客 Vim 配置入门 - 阮一峰的网络日志
" 默认的 Vim 配置参考 /etc/vim/vimrc 或者 /etc/vimrc，本文件是用户配置

syntax enable       " 开启语法高亮
syntax on           " 允许用指定语法高亮配色方案替换默认方案

set showmode        " 底部显示 vim 模式
set showcmd         " 命令模式下，显示键入的指令
set number          " 显示行号
set ruler           " 显示标尺
set cursorline      " 高亮当前行（下划线）
"set cursorcolumn    " 高亮当前列

set shiftwidth=2    " 设定 <<（增加一级缩进）、>>（取消一级缩进）、==（取消全部缩进） 命令移动时的宽度为 4
set tabstop=2       " Tab 键的长度为 4 个空格
set softtabstop=2   " 用 4 个空格直接代替 Tab
set autoindent      " 自动缩进
set expandtab       " 自动把 Tab 转为空格
set tw=100          " 字符超过 100 个有颜色提示

set nocompatible    " 去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限
set backspace=indent,eol,start  " 定义删除键
set scrolloff=5     " 光标移动到顶部或者底部时，保持几行距离
set history=10000   " 历史命令记录条数
set mouse=v         " 设置 vim 下可以拷贝到 clipboard

set autochdir       " 自动把工作目录切换到当前编辑的文件下
set autoread        " 打开文件监视，如果编辑过程发生外部改变（被别的编辑器修改），就会发出提示
set hlsearch        " 高亮检索结果
set incsearch       " 检索时每输入一个字符，就自动跳到第一个匹配的结果

set nobackup        " 不备份，备份文件是在原文件的末尾加上一个波浪号
"set noswapfile     " 不创建交换文件
set undofile        " 保留撤销历史，即使文件已经被关闭和再次打开

" 自动缩进
filetype indent on

" 让配置变更立即生效
autocmd BufWritePost $MYVIMRC source $MYVIMRC

" vim 主题
colorscheme desert
" colorscheme solarized

" 中文编码相关
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

" 设置备份文件、交换文件、操作历史文件的保存位置（需要先创建文件夹）
"set backupdir=~/.vim/.backup//
"set directory=~/.vim/.swap//
"set undodir=~/.vim/.undo//

" 如果行尾有多余的空格（包括 Tab 键），该配置将让这些空格显示成可见的小方块
set list
set listchars=tab:>-,trail:~

" 命令模式下的 Tab 自动补全（貌似不起作用）
set wildmenu
set wildmode=longest:list,full

" 自动补全
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

" 重新打开文件时，记住上次编辑的位置
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

" 状态栏，让编辑器底部显示编辑的文件名
set laststatus=2
set statusline=%{fnamemodify(resolve(expand('%:p')),':~')}\ %*

" Vundle 插件
" 需要先安装 Vundle，git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
set nocompatible              " be iMproved, required
filetype off                  " required
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'itchyny/lightline.vim'
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'Yggdroot/indentLine'
Plugin 'kshenoy/vim-signature'
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/nerdtree'
Plugin 'airblade/vim-gitgutter'

call vundle#end()            " required
filetype plugin indent on    " required
" end of Vundle 插件

" for lightline
if !has('gui_running')
  set t_Co=256
endif

" Plugin for vim-cpp-enhanced-highlight
let g:cpp_member_variable_highlight = 1
let g:cpp_class_scope_highlight = 1
let g:cpp_class_decl_highlight = 1


""""""""""""""""""""""""Plugin YouCompleteMe""""""""""""""""""""""""

" YCM 补全菜单配色
" 菜单
"highlight Pmenu ctermfg=2 ctermbg=3 guifg=#005f87 guibg=#EEE8D5
" 选中项
"highlight PmenuSel ctermfg=2 ctermbg=3 guifg=#AFD700 guibg=#106900
" 补全功能在注释中同样有效
let g:ycm_complete_in_comments=1
" 允许 vim 加载 .ycm_extra_conf.py 文件，不再提示
"let g:ycm_confirm_extra_conf=0
" 配置全局 .ycm_extra_conf.py 文件
let g:ycm_global_ycm_extra_conf='~/.ycm_extra_conf.py'
" 开启 YCM 标签补全引擎
let g:ycm_collect_identifiers_from_tags_files=1
" 引入 C++ 标准库tags
set tags+=/data/misc/software/misc./vim/stdcpp.tags
" YCM 集成 OmniCppComplete 补全引擎，设置其快捷键
inoremap <leader>; <C-x><C-o>
" 补全内容不以分割子窗口形式出现，只显示补全列表
set completeopt-=preview
" 从第一个键入字符就开始罗列匹配项
let g:ycm_min_num_of_chars_for_completion=1
" 禁止缓存匹配项，每次都重新生成匹配项
let g:ycm_cache_omnifunc=0
" 语法关键字补全
let g:ycm_seed_identifiers_with_syntax=1

""""""""""""""""""""""""Plugin YouCompleteMe""""""""""""""""""""""""


""""""""""""""""""""""""Plugin NerdTree""""""""""""""""""""""""

" 使用 NERDTree 插件查看工程文件。设置快捷键，速记：file list
nmap <Leader>fl :NERDTreeToggle<CR>
" 设置NERDTree子窗口宽度
let NERDTreeWinSize=32
" 设置NERDTree子窗口位置
let NERDTreeWinPos="right"
" 显示隐藏文件
let NERDTreeShowHidden=1
" NERDTree 子窗口中不显示冗余帮助信息
let NERDTreeMinimalUI=1
" 删除文件时自动删除文件对应 buffer
let NERDTreeAutoDeleteBuffer=1

""""""""""""""""""""""""Plugin NerdTree""""""""""""""""""""""""


""""""""""""""""""""""""Plugin vim-gitgutter""""""""""""""""""""""""
" Use fontawesome icons as signs
let g:gitgutter_sign_added = '+'
let g:gitgutter_sign_modified = '>'
let g:gitgutter_sign_removed = '-'
let g:gitgutter_sign_removed_first_line = '^'
let g:gitgutter_sign_modified_removed = '<'

let g:gitgutter_override_sign_column_highlight = 1
highlight SignColumn guibg=#404040
highlight SignColumn ctermbg=404040

set updatetime=250

""""""""""""""""""""""""Plugin vim-gitgutter""""""""""""""""""""""""

```
