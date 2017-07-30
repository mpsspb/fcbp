/**
* Personal
* @namespace fcbp.personal.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.personal.directives')
    .directive('personal', personal);


  var DirectControl = function($scope, Personals, Periods, Positions) {
    var vm = this;
    vm.success = false;
    vm.error = false;
    vm.error_data = '';

    vm.active = function () {
      Personals.active($scope.personal.id).then(personalSuccessFn, personalErrorFn);

      function personalSuccessFn(data, status, headers, config) {
        $scope.personal = data.data;
      }
      function personalErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    vm.update = function() {
      var fdata = {};
      angular.copy($scope.personal, fdata);
      delete fdata['positions']
      Personals.update($scope.personal.id, fdata).then(updSuccessFn, updErrorFn);

      function updSuccessFn(data, status, headers, config) {
        $scope.personal = data.data;
        vm.success = true;
      }
      function updErrorFn(data, status, headers, config) {
        vm.error = true;
        vm.error_data = data.data;
        console.log(data);
      }

    };

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {
      Periods.list().then(periodsSuccessFn, periodsErrorFn);

      /**
      * @name periodsSuccessFn
      * @desc Update ClubCard array on view
      */
      function periodsSuccessFn(data, status, headers, config) {
        vm.periods = data.data;
      }

      /**
      * @name periodsErrorFn
      * @desc console log error
      */
      function periodsErrorFn(data, status, headers, config) {
        console.log(data);
      };

      Positions.list().then(positionsSuccessFn, positionsErrorFn);

      /**
      * @name positionsSuccessFn
      * @desc Update Positions array on view
      */
      function positionsSuccessFn(data, status, headers, config) {
        vm.positions = data.data;
      }

      /**
      * @name positionsErrorFn
      * @desc console log error
      */
      function positionsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };
    
    activate();

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
      controller: DirectControl,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/personal.html?8066'
    };

    return directive;
  }
})();