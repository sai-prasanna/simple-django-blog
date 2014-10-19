$(function(){
    $("#typed").typed({
    strings: ["Hi,\nI am Sai Prasanna.\nI am a software developer from chennai,\nwho likes contemplating at the universe,\nprogramming and reading books.\n\nWelcome to my blog"],
    typeSpeed: 100, // typing speed
    backSpeed: 0, // backspacing speed
    startDelay: 0, // time before typing starts
    backDelay: 0, // pause before backspacing
    loop: false, // loop on or off (true or false)
    loopCount: false, // number of loops, false = infinite
    showCursor: true,
    attr: null, // attribute to type, null = text for everything except inputs, which default to placeholder
    });
});
