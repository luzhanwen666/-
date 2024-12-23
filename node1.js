var $_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
var _chars_len = $_chars.length;
function rds(len) {
    var retStr = '';
    for (i = 0; i < len; i++) {
        retStr += $_chars.charAt(Math.floor(Math.random() * _chars_len));
    }
    return retStr;
}
