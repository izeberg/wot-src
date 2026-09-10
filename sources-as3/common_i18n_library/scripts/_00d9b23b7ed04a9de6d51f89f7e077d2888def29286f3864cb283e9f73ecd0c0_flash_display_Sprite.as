package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _00d9b23b7ed04a9de6d51f89f7e077d2888def29286f3864cb283e9f73ecd0c0_flash_display_Sprite extends Sprite
   {
       
      
      public function _00d9b23b7ed04a9de6d51f89f7e077d2888def29286f3864cb283e9f73ecd0c0_flash_display_Sprite()
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
