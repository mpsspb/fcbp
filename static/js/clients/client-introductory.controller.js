/**
* ClientIntroductoryController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ClientIntroductoryController', ClientIntroductoryController);

  ClientIntroductoryController.$inject = ['$rootScope', '$scope', '$routeParams', 'Clients' , 'Employees'];

  /**
  * @namespace ClientIntroductoryController
  */
  function ClientIntroductoryController($rootScope, $scope, $routeParams, Clients, Employees) {
    var vm = this;

    vm.submit = submit;
    vm.uid = $routeParams.uid;

    activate();

    function activate() {

      Clients.get(vm.uid).then(cardclientSuccessFn, cardclientErrorFn);
        /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.fdata = data.data;
        vm.fdata['introductory_date'] = moment(vm.fdata['introductory_date'], 'YYYY-MM-DD HH:mm').format('DD.MM.YYYY HH:mm')
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Employees.list().then(listEmployeeSuccessFn, listEmployeeErrorFn);
    
      /**
      * @name listEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function listEmployeeSuccessFn(data, status, headers, config) {
        vm.employees = data.data;
      }

      /**
      * @name listEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function listEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
      }
    }

    /**
    * @name submit
    * @desc Create a new Client
    * @memberOf fcbp.client.controllers.ClientIntroductoryController
    */
    function submit() {

      Clients.introductory(vm.uid, vm.fdata).then(createClientSuccessFn, createClientErrorFn);


      /**
      * @name createClientSuccessFn
      * @desc Show snackbar with success message
      */
      function createClientSuccessFn(data, status, headers, config) {
        window.location = '#/cardclient/' + vm.uid + '/';
      }


      /**
      * @name createClientErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createClientErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('Client.created.error');
      }
    }
    
  };

})();