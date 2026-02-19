$(document).ready(function () {
  

  var ele = document.getElementById('app');
  var app = new Vue({
    el: ele,
    data: {
      i: 0,
      i2: 0,

    },
    methods: {
      ren: (min, max) => { return Math.floor(Math.random() * (max - min + 1)) + min; },

      rand: (a, s) => {
        function rsan(min, max) {
          return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        var aa = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
        var ss = "";
        for (let i = a; i < s; i++) {
          ss += aa.charAt(rsan(0, aa.length - 1))
        }
        return ss
      },
      txt1: (st1, dd, tt) => {
        var textFile = null,
          makeTextFile = function (text) {
            var data = new Blob([text], { type: "text/plain" });
            if (textFile !== null) { window.URL.revokeObjectURL(textFile); }
            textFile = window.URL.createObjectURL(data);
            return textFile;
          };

        var create = document.getElementById("downloadCode");
        a = document.createElement("a"); // Create link.
        document.body.appendChild(a); // Set link on DOM.
        a.style = "display: none"; // Make link unvisible on the screen.
        a.href = makeTextFile(st1); // Set href on link.
        a.setAttribute("download", dd + "." + tt); // To open the download dialog
        a.click(); // Trigger click of link.
      },
      chin:()=>{
        var hosini = $('#txtt1').val()
        var oo2 = 0; var ss = 0;
        var i1 = 0; var i2 = 0; var i3 = 0; var dd = ""; var bol = true; var hosini2 = [];
        for (let i = 0; i < hosini.length; i++) {
          hosini2[i] = Habib[$('#index').val()][i2];
          i2++;
          if (i2 == Habib[$('#index').val()].length - 1) i2 = 0
        }
        for (let i = 0; i < hosini.length; i++) {
          ss = hosini.charCodeAt(i);
          dd += String.fromCodePoint(ss + hosini2[i])
        }
        $('#txtt2').val(dd);
      },
      chdn:()=>{
        var hosini = $('#txtt1').val()
        var oo2 = 0; var ss = 0; var dd = ""; var bol = true;
        var i1 = 0; var i2 = 0; var i3 = 0; var dd = ""; var bol = true; var hosini2 = [];
        for (let i = 0; i < hosini.length; i++) {
          hosini2[i] = Habib[$('#index').val()][i2];
          i2++;
          if (i2 == Habib[$('#index').val()].length - 1) i2 = 0
        }
        for (let i = 0; i < hosini.length; i++) {
          ss = hosini.charCodeAt(i);
          dd += String.fromCodePoint(ss - hosini2[i])
        }
        $('#txtt2').val(dd);
      },
       aa5:()=>{
        
       },
      // aa5:()=>{},
      // aa5:()=>{},
      // aa5:()=>{},
      // aa5:()=>{},

    }

  });

});