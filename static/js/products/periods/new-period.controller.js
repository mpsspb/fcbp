/**
* NewPeriodController
* @namespace fcbp.periods.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.periods.controllers')
    .controller('NewPeriodController', NewPeriodController);

  NewPeriodController.$inject = ['$rootScope', '$scope', 'Periods'];

  /**
  * @namespace NewPeriodController
  */
  function NewPeriodController($rootScope, $scope, Periods) {
    var vm = this;

    vm.submit = submit;

    vm.fdata = { is_month: true, }

    /**
    * @name submit
    * @desc Create a new Period
    * @memberOf fcbp.periods.controllers.NewPeriodController
    */
    function submit() {

      $rootScope.$broadcast('period.created', vm.fdata );

      Periods.create(vm.fdata).then(createPeriodSuccessFn, createPeriodErrorFn);


      /**
      * @name createPeriodSuccessFn
      * @desc Show snackbar with success message
      */
      function createPeriodSuccessFn(data, status, headers, config) {
        console.log('Success! Period created.');
      }


      /**
      * @name createPeriodErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPeriodErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('period.created.error');
      }
    }

  }

})();