$(function() {

    // Compare substrings when length has focus
    // directly from pset6
    $('input[name=length]').focus(function() {
        $('input[name=algorithm][value=substrings]').prop('checked', true);
    });

});