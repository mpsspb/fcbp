/**
* NewDiscountController
* @namespace fcbp.discounts.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.discounts.controllers')
    .controller('NewDiscountController', NewDiscountController);

  NewDiscountController.$inject = ['$rootScope', '$scope', 'Discounts'];

  /**
  * @namespace NewDiscountController
  */
  function NewDiscountController($rootScope, $scope, Discounts) {
    var vm = this;

    vm.submit = submit;

    vm.fdata = {};

    /**
    * @name submit
    * @desc Create a new Discount
    * @memberOf fcbp.discounts.controllers.NewDiscountController
    */
    function submit() {

      Discounts.create(vm.fdata).then(createSportSuccessFn, createSportErrorFn);


      /**
      * @name createSportSuccessFn
      * @desc Show snackbar with success message
      */
      function createSportSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('discount.created', vm.fdata );
        console.log('Success! Discount created.');
        vm.fdata = {};
      }


      /**
      * @name createSportErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createSportErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('discount.created.error');
      }
    }

  }

})();