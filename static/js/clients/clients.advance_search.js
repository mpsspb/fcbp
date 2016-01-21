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
      'last_name': 'Фамилия',
      'first_name': 'Имя',
      'patronymic': 'Отчетво',
      'born': 'Дата рождения',
      'uid': 'ЧС',
      // 'clubcard': 'Клубная'
    }

    vm.search_text = '';
    vm.fsearch = [];
    vm.addSearch = addSearch;
    vm.removeSearch = removeSearch;
    vm.clients = [];
    vm.searchClient = searchClient;

    /**
    * add search option
    **/
    function addSearch() {

      if (!vm.search_object ) {
        vm.err_search_object = true
        return
      } else {
        vm.err_search_object = false
      }

      if (vm.search_text.length < 3 ) {
        vm.err_search_text = true
        return
      } else {
        vm.err_search_text = false
      }
      vm.fsearch.push({'search_object': vm.search_object,
                       'search_text': vm.search_text,
                     });
      vm.search_text = ''
      vm.search_object = ''
    };

    /**
    * remove search option
    **/
    function removeSearch(key) {
      vm.fsearch.splice(key, 1);
    }

    /**
    * @name searchClient
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.AdvanceSearchController
    */
    function searchClient() {
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