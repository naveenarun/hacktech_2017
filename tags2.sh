# tags system explained: http://arstechnica.com/apple/2013/10/os-x-10-9/9/
local src=$1
local action="get"

if [[ $src == "-add" ]]; then
    src=$3
    local newtag=$2
    local action="add"
fi

# hex -> bin -> json -> lines
local hexToLines="xxd -r -p - - | plutil -convert json -o - - | sed 's/[][]//g' | tr ',' '\n'"

# lines -> json -> bin -> hex
local linesToHex="tr '\n' ',' | echo [\$(sed 's/,$//')] | plutil -convert binary1 -o - - | xxd -p - -"

local gettags="xattr -px com.apple.metadata:_kMDItemUserTags \"$src\" 2> /dev/null | $hexToLines | sed 's/.*Property List error.*//'"

if [[ $action == "get" ]]; then
    sh -c "$gettags"
else
    local add="(cat -; echo \\\"$newtag\\\") | sort -u"
    local write="xattr -wx com.apple.metadata:_kMDItemUserTags \"\$($gettags | $add | grep . | $linesToHex)\" \"$src\""

    sh -c "$write"
fi
