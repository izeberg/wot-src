package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ccc617c41e009994d1eff63e4e2b5bf3a8d83ee8943e76b9a148e6838258b1e1_flash_display_Sprite extends Sprite
   {
       
      
      public function _ccc617c41e009994d1eff63e4e2b5bf3a8d83ee8943e76b9a148e6838258b1e1_flash_display_Sprite()
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
