package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8b2f70adfad0ac7b77aa6776787461fac5c764a90636ffef735f4b76bf1b1b9e_flash_display_Sprite extends Sprite
   {
       
      
      public function _8b2f70adfad0ac7b77aa6776787461fac5c764a90636ffef735f4b76bf1b1b9e_flash_display_Sprite()
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
