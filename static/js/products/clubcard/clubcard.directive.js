/**
* ClubCard
* @namespace fcbp.clubcard.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clubcard.directives')
    .directive('clubcard', clubcard);

  var DirectControl = function($scope, ClubCard, Periods) {
    var vm = this;
    vm.success = false;
    vm.error = false;
    vm.error_data = '';

    vm.active = function () {
      ClubCard.active($scope.clubcard.id).then(clubcardSuccessFn, clubcardErrorFn);

      function clubcardSuccessFn(data, status, headers, config) {
        $scope.clubcard = data.data;
      }
      function clubcardErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    vm.update = function() {
      ClubCard.update($scope.clubcard.id, $scope.clubcard).then(updSuccessFn, updErrorFn);

      function updSuccessFn(data, status, headers, config) {
        $scope.clubcard = data.data;
        vm.success = true;
      }
      function updErrorFn(data, status, headers, config) {
        vm.error = true;
        vm.error_data = data.data;
        console.log(data);
      }

    }

    activate();

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
      }

    }
  
  };

  /**
  * @namespace ClubCard
  */
  function clubcard() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.clubcard.directives.ClubCard
    */
    var directive = {
      restrict: 'E',
      scope: {
        clubcard: '='
      },
      controller: DirectControl,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/clubcard.html?1'
    };

    return directive;
  }
})();