(function () {
  'use strict';

  angular
    .module('fcbp')
    .filter('period_str', function() {
        return function(input) {
          if (input.is_month){
            if (input.value < 2) {
              return '1 месяц'
            } else if ( input.value < 5) {
              return input.value + ' месяца'
            } else {
              return input.value + ' месяцев'
            }
          } else {
            if (input.value < 2) {
              return '1 день'
            } else if ( input.value < 5) {
              return input.value + ' дня'
            } else {
              return input.value + ' дней'
            }            
          }

          
        }
    });

  angular
    .module('fcbp')
    .filter('visits', function() {
        return function(input) {
          if (input == 99999) {
            return 'Безлимитное'
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

  angular
    .module('fcbp')
    .filter('YN', function() {
        return function(input) {
          if (input) {
            return 'Да'
          } else {
            return 'Нет'
          }
          
        }
    });

  angular
    .module('fcbp')
    .filter('phone', function() {
        return function(input) {
          if (input ) {
            input = input.toString()
            if (input.length == 7) {
              return input.substr(0,3) + ' - ' + input.substr(3)
            } else if (input.length == 10) {
              var mobile = '+7 (' + input.substr(0,3) + ') ' +
                       input.substr(3,3) + ' - ' + input.substr(6)
              return mobile
            } else {
              return input
            }
          }
          
        }
    });

})();