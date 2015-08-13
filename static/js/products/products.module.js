(function () {
  'use strict';

  angular
    .module('fcbp.products', [
      'fcbp.periods.controllers',
      'fcbp.clubcard.controllers',
      'fcbp.clubcard.directives',
      'fcbp.aquaaerobics.controllers',
      'fcbp.aquaaerobics.directives',
      'fcbp.sports.controllers',
    ]);

  angular
    .module('fcbp.periods.controllers', [])

  angular
    .module('fcbp.clubcard.controllers', [])

  angular
    .module('fcbp.clubcard.directives', [])

  angular
    .module('fcbp.aquaaerobics.controllers', [])

  angular
    .module('fcbp.aquaaerobics.directives', [])

  angular
    .module('fcbp.sports.controllers', [])

})();