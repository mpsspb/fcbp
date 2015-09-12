/**
* ClientCardController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ClientCardController', ClientCardController);

  ClientCardController.$inject = ['$rootScope', '$routeParams', '$scope', 'Clients'];

  /**
  * @namespace ClientCardController
  */
  function ClientCardController($rootScope, $routeParams, $scope, Clients) {
    var vm = this;

    activate();
    vm.cardclient = {};
    vm.go = function(name){
      alert(name)
    }

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {

      var uid = $routeParams.uid
      Clients.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.cardclient = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();