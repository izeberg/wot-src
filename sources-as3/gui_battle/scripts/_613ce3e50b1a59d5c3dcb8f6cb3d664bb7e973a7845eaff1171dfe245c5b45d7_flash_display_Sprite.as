package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _613ce3e50b1a59d5c3dcb8f6cb3d664bb7e973a7845eaff1171dfe245c5b45d7_flash_display_Sprite extends Sprite
   {
       
      
      public function _613ce3e50b1a59d5c3dcb8f6cb3d664bb7e973a7845eaff1171dfe245c5b45d7_flash_display_Sprite()
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
