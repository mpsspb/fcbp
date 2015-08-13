/**
* NewSportController
* @namespace fcbp.sports.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.sports.controllers')
    .controller('NewSportController', NewSportController);

  NewSportController.$inject = ['$rootScope', '$scope', 'Sports'];

  /**
  * @namespace NewSportController
  */
  function NewSportController($rootScope, $scope, Sports) {
    var vm = this;

    vm.submit = submit;

    vm.fdata = {};

    /**
    * @name submit
    * @desc Create a new Sport
    * @memberOf fcbp.sports.controllers.NewSportController
    */
    function submit() {

      Sports.create(vm.fdata).then(createSportSuccessFn, createSportErrorFn);


      /**
      * @name createSportSuccessFn
      * @desc Show snackbar with success message
      */
      function createSportSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('sport.created', vm.fdata );
        console.log('Success! Sport created.');
      }


      /**
      * @name createSportErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createSportErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('sport.created.error');
      }
    }

  }

})();