(function () {
  'use strict';

  angular
    .module('fcbp.archive.routes', ['ngRoute']);
    
  angular
    .module('fcbp.archive.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/archive/:uid', {
      controller: 'ArchiveController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/archive/archive.html'
    }).when('/archive/clubcard/:uid', {
      controller: 'UseClientCardController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/archive/clubcard.html'
    }).when('/archive/aquaaerobics/:uid', {
      controller: 'UseClientAquaController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/archive/aquaaerobics.html'
    })
  }
})();