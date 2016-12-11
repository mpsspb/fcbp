/**
* AdvanceSearchController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('AdvanceSearchController', AdvanceSearchController);

  AdvanceSearchController.$inject = ['$scope', '$http',
                               'Authentication', 'ClubCard', 'Clients'];

  /**
  * @namespace AdvanceSearchController
  */
  function AdvanceSearchController($scope, $http, Authentication, ClubCard, Clients) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    vm.search_objects = {
      'fio': 'ФИО',
      'last_name': 'Фамилия',
      'first_name': 'Имя',
      'patronymic': 'Отчество',
      'born': 'Дата рождения',
      'uid': 'ЧС',
      'email': 'e-mail',
      'mobile': 'телефон'
    }

    vm.fsearch = [];
    vm.clients = [];
    vm.comparison = 0;
    vm.searchClient = searchClient;

    /**
    * @name searchClient
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.AdvanceSearchController
    */
    function searchClient() {
      vm.fsearch = {'search_object': vm.search_object,
                    'search_text': vm.search_text,
                    'comparison': vm.comparison,
                    };
      console.log(vm.fsearch)
      Clients.advanced_search({'params': vm.fsearch}).then(clientsSuccessFn, clientsErrorFn);

      /**
      * @name clientsSuccessFn
      * @desc Update Clients array on view
      */
      function clientsSuccessFn(data, status, headers, config) {
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
    * @memberOf fcbp.clients.controllers.AdvanceSearchController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();