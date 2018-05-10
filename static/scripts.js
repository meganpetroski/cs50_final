$(function() {

    // Compare substrings when length has focus from pset 6
    $('input[name=length]').focus(function() {
        $('input[name=algorithm][value=substrings]').prop('checked', true);
    });

});