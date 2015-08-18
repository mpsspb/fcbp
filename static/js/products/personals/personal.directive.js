/**
* Personal
* @namespace fcbp.personal.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.personal.directives')
    .directive('personal', personal);

  /**
  * @namespace Personal
  */
  function personal() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.personal.directives.Personal
    */
    var directive = {
      restrict: 'E',
      scope: {
        personal: '='
      },
      templateUrl: '/static/templates/products/personal.html?1'
    };

    return directive;
  }
})();