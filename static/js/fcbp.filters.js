(function () {
  'use strict';

  angular
    .module('fcbp')
    .filter('monthes', function() {
        return function(input) {
          if (input < 2) {
            return '1 месяц'
          } else if ( input < 5) {
            return input + ' месяца'
          } else {
            return input + ' месяцев'
          }
          
        }
    });
 
})();