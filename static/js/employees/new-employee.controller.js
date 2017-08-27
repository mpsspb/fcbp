/**
* NewEmployeeController
* @namespace fcbp.employees.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.controllers')
    .controller('NewEmployeeController', NewEmployeeController);

  NewEmployeeController.$inject = ['$scope', '$http', '$routeParams',
  'Positions' , 'Employees'];

  /**
  * @namespace NewEmployeeController
  */
  function NewEmployeeController($scope, $http, $routeParams, Positions, Employees ) {
    var vm = this;

    vm.submit = submit
    vm.uid = $routeParams.uid

    if ( vm.uid != undefined ){
      activate();
    }

    function activate() {

      Employees.get(vm.uid).then(cardempSuccessFn, cardempErrorFn);

      /**
      * @name cardempSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardempSuccessFn(data, status, headers, config) {
        vm.fdata = data.data;
        vm.fdata.born = moment(vm.fdata.born, 'YYYY-MM-DD').format('DD.MM.YYYY');
      }

      /**
      * @name cardempErrorFn
      * @desc console log error
      */
      function cardempErrorFn(data, status, headers, config) {
        console.log(data);
      }

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

    function submit() {
      console.log(vm.uid)
      if ( vm.uid == undefined ){
        Employees.create(vm.fdata).then(createEmployeeSuccessFn, createEmployeeErrorFn);
      } else {
        Employees.edit(vm.uid, vm.fdata).then(createEmployeeSuccessFn, createEmployeeErrorFn);
      }
    
      /**
      * @name createEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function createEmployeeSuccessFn(data, status, headers, config) {
        console.log('Success! Employee created.');
        window.location = '/#/employees-list';
      }


      /**
      * @name createEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('Employee.created.error');
      }

    }

  }
})();