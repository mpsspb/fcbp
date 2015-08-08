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

  angular
    .module('fcbp')
    .filter('visits', function() {
        return function(input) {
          if (input == 99999) {
            return 'Безлитиное'
          } else {
            return input
          }
          
        }
    });

  angular
    .module('fcbp')
    .filter('card_time', function() {
        return function(input) {
          if (input) {
            return 'Полное'
          } else {
            return 'Утро'
          }
          
        }
    });

  angular
    .module('fcbp')
    .filter('EN', function() {
        return function(input) {
          if (input) {
            return 'Есть'
          } else {
            return 'Нет'
          }
          
        }
    });

})();