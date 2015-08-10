(function () {
  'use strict';

  angular
    .module('fcbp.clients', [
      'fcbp.clients.controllers',
      'fcbp.clients.services',
      'fcbp.client.directives',
    ]);

  angular
    .module('fcbp.clients.controllers', ['webcam']);

  angular
    .module('fcbp.clients.services', []);

  angular
    .module('fcbp.client.directives', [])

})();