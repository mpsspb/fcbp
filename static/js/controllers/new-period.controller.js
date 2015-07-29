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

    /**
    * @name submit
    * @desc Create a new Period
    * @memberOf fcbp.periods.controllers.NewPeriodController
    */
    function submit() {
      $rootScope.$broadcast('post.created', {
        content: vm.content,
      });

      $scope.closeThisDialog();

      Periods.create(vm.content).then(createPeriodSuccessFn, createPeriodErrorFn);


      /**
      * @name createPeriodSuccessFn
      * @desc Show snackbar with success message
      */
      function createPeriodSuccessFn(data, status, headers, config) {
        // Snackbar.show('Success! Post created.');
      }


      /**
      * @name createPeriodErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createPeriodErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('post.created.error');
        // Snackbar.error(data.error);
      }
    }
  }
})();