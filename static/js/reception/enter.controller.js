/**
* EnterController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('EnterController', EnterController);

  EnterController.$inject = ['$scope', '$location', 'Authentication', 'Clients'];

  /**
  * @namespace EnterController
  */
  function EnterController($scope, $location, Authentication, Clients) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.submit = submit;

    function submit() {

      Clients.search(vm.fdata).then(clientsSuccessFn, clientsErrorFn);

      /**
      * @name clientsSuccessFn
      * @desc Update Clients array on view
      */
      function clientsSuccessFn(data, status, headers, config) {
        vm.clients = data.data
        if (vm.clients.length == 1) {
          $location.url('/cardclient/' + vm.clients[0].id)
        }
      }

      /**
      * @name clientsErrorFn
      * @desc console log error
      */
      function clientsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.EnterController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    }

  }
})();