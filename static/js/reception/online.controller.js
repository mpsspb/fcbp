/**
* OnlineController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('OnlineController', OnlineController);

  OnlineController.$inject = ['$scope', 'Authentication', 'Clients'];

  /**
  * @namespace OnlineController
  */
  function OnlineController($scope, Authentication, Clients) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    activate();

    function activate() {
      Clients.online().then(clientsSuccessFn, clientsErrorFn);

      /**
      * @name clientsSuccessFn
      * @desc Update Clients array on view
      */
      function clientsSuccessFn(data, status, headers, config) {
        // console.log(data);
        vm.clients = data.data
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
    * @memberOf fcbp.layout.controllers.OnlineController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    }

  }
})();