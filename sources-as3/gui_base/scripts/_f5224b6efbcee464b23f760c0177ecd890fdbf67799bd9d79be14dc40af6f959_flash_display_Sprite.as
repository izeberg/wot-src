package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f5224b6efbcee464b23f760c0177ecd890fdbf67799bd9d79be14dc40af6f959_flash_display_Sprite extends Sprite
   {
       
      
      public function _f5224b6efbcee464b23f760c0177ecd890fdbf67799bd9d79be14dc40af6f959_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
