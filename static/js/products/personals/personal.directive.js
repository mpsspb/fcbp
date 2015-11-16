/**
* Personal
* @namespace fcbp.personal.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.personal.directives')
    .directive('personal', personal);


  var active = function($scope, Personals) {
    var vm = this;
    vm.active = function () {
      Personals.active($scope.personal.id).then(personalSuccessFn, personalErrorFn);

      function personalSuccessFn(data, status, headers, config) {
        $scope.personal = data.data;
      }
      function personalErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  };
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
      controller: active,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/personal.html?1'
    };

    return directive;
  }
})();